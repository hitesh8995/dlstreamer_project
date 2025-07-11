import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)

# === Configurable parameters ===
VIDEO_PATH = "/data/video.mp4"
DETECTION_MODEL = "/models/detection/person-detection-retail-0013.xml"
CLASSIFICATION_MODEL = "/models/classification/person-attributes-recognition-crossroad-0230.xml"
NUM_STREAMS = 8
  # <-- Change this to test more streams
DEVICE = "CPU"  # or "GPU" if GPU is configured

# === Build one stream branch ===
def build_stream(index):
    return f"""
        filesrc location={VIDEO_PATH} !
        decodebin !
        videoconvert !
        gvadetect model={DETECTION_MODEL} device={DEVICE} !
        gvaclassify model={CLASSIFICATION_MODEL} device={DEVICE} !
        queue !
        gvametaconvert !
        gvafpscounter name=fps{index} !
        fakesink sync=false
    """

# === Build full pipeline with N streams ===
pipeline_str = " ".join([build_stream(i) for i in range(NUM_STREAMS)])
print(f"[INFO] Launching pipeline with {NUM_STREAMS} streams on {DEVICE}")

pipeline = Gst.parse_launch(pipeline_str)
pipeline.set_state(Gst.State.PLAYING)

# === Monitor messages ===
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

pipeline.set_state(Gst.State.NULL)
