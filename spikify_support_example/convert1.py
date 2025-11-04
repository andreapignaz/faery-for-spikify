import faery

d = "Example of a spikified output"
a = "00:00:01.0"
b = "00:00:02.0"

(
    faery.events_stream_from_file('sasso-orig.aedat4')
    .time_slice(start=a, end=b)
    .to_file('sasso-spiky.aedat4', spikify=True, spikify_description=d)
)