import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# Initialize GStreamer
Gst.init(None)

# File & model paths inside the container
VIDEO_PATH = "/data/video.mp4"
DETECTION_MODEL = "/models/detection/person-detection-retail-0013.xml"
CLASSIFICATION_MODEL = "/models/classification/person-attributes-recognition-crossroad-0230.xml"

# Define GStreamer pipeline
pipeline_str = f"""
    filesrc location={VIDEO_PATH} !
    decodebin !
    gvadetect model={DETECTION_MODEL} device=CPU !
    gvaclassify model={CLASSIFICATION_MODEL} device=CPU !
    gvametaconvert !
    gvafpscounter !
    fakesink sync=false
"""

# Launch pipeline
pipeline = Gst.parse_launch(pipeline_str)
pipeline.set_state(Gst.State.PLAYING)

# Wait until finished
bus = pipeline.get_bus()
while True:
    msg = bus.timed_pop_filtered(
        Gst.CLOCK_TIME_NONE,
        Gst.MessageType.ERROR | Gst.MessageType.EOS
    )
    if msg:
        if msg.type == Gst.MessageType.ERROR:
            err, debug = msg.parse_error()
            print(f"[ERROR] {err}: {debug}")
            break
        elif msg.type == Gst.MessageType.EOS:
            print("[INFO] End of stream.")
            break

# Clean up
pipeline.set_state(Gst.State.NULL)
