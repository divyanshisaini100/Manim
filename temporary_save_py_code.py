import zipfile

with zipfile.ZipFile("animated_final_vid.zip", "w") as zipf:
    zipf.write("GA_Q1/media/videos/main/480p15/ga_q1.mp4", arcname="ga_q1.mp4") 