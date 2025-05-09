import cv2
import pandas as pd
import os

def get_videos_from_folder(folder):
    """Loads all video files from a folder."""
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.mp4', '.avi'))]

def play_video(video_path, speed=4.0):
    """Plays a video at a given speed (lower = faster)."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS) / speed)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(fps) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def analyze_video(video_path, case_number, num_people, note, interval=4):
    """Analyzes video frames at fixed intervals with manual annotation."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return []

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval_frames = interval * fps
    results = []

    for i in range(0, frame_count, interval_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video", frame)
        cv2.waitKey(1)

        for person in range(num_people):
            label = "Participant" if person == 0 else f"Person {person}"
            while True:
                zone = input(f"Enter zone for {label} (i/p/s/x): ").strip().lower()
                if zone in ['i', 'p', 's', 'x']:
                    break
                print("Invalid input. Use: i = intimate, p = personal, s = social, x = off-screen")

            results.append({
                "Case": case_number,
                "Timestamp (s)": round(i / fps, 2),
                "Person": "Participant" if person == 0 else f"Person {person}",
                "Zone": "Off-screen" if zone == 'x' else zone,
                "Note": note
            })

    cap.release()
    cv2.destroyAllWindows()
    return results

def save_results_to_excel(results, output_file):
    """Saves annotated results to Excel, avoiding duplicates."""
    if os.path.exists(output_file):
        df_existing = pd.read_excel(output_file)
        df_new = pd.DataFrame(results)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True).drop_duplicates()
    else:
        df_combined = pd.DataFrame(results)

    df_combined.to_excel(output_file, index=False)
    print(f"Results saved to: {output_file}")

def main():
    """Main routine for video analysis."""
    base_folder = input("Enter the folder containing the videos: ").strip()
    if not os.path.exists(base_folder):
        print("Folder does not exist.")
        return

    output_file = os.path.join(base_folder, "analysis_results.xlsx")
    videos = get_videos_from_folder(base_folder)

    if not videos:
        print(f"No video files found in {base_folder}.")
        return

    all_results = []
    for video in videos:
        case_number = os.path.splitext(os.path.basename(video))[0]
        play_video(video, speed=5.0)

        while True:
            try:
                num_people = int(input("How many people are visible in the video? "))
                if num_people >= 1:
                    break
                else:
                    print("Please enter at least 1.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        note = input("Enter an optional note for this video: ").strip()
        results = analyze_video(video, case_number, num_people, note, interval=4)
        all_results.extend(results)
        save_results_to_excel(all_results, output_file)

    print("✅ Annotation complete.")

if __name__ == "__main__":
    main()
