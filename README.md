# Group-Proximity-Annotation-Tool-for-Human-Agent-Interaction
This Python-based tool allows for manual video annotation of group interactions, specifically designed for analyzing spatial behavior in Human-Robot Interaction (HRI) and Human-Agent Interaction, social dynamics and proximity studies. It was developed for studies on **group-agent interactions** and allows manual annotation of proximity zones based on Hall’s proxemic theory [1] (intimate, personal, social, + off-screen).

## 🖱 Demo

Here's how the GPAT works

![Group-Proximity-Annotation-Tool-for-Human-Agent-Interaction](Demo_Video_GPAT_reduced.gif)
[The person shown in the video is not a study participant, but a colleague who interacted with the Furhat robot for demonstration purposes. The interaction was recorded in summer 2024 at the Deutsches Museum Bonn during one of the two field studies in which the GPAT was used. The video shows the interaction from two different camera perspectives.]
  
## 🎯 Purpose

Designed to support **frame-based manual coding**, this tool allows researchers to:

- Load and preview `.mp4` or `.avi` video files
- Annotate proximity zones at regular time intervals
- Enter observations per person (e.g. Participents, Group Member (GM) 1, GM2, …)
- Export structured data to Excel for further analysis


## 📦 Dependencies

Install required libraries: pip install opencv-python pandas
GPTA was tested with Python 3.13.1

## 🛠 Features
-	📽 Video playback with adjustable speed
-	⏱ Interval-based frame capture for annotation
-	👤 Multi-person coding interface
-	💾 Excel export

 ## 📁 File Overview
-	proximity_annotation.py: Main script

 ## 🚀 Usage

 python proximity_annotation.py

 You will be prompted to:
	1.	Select a folder containing your videos
	2.	Play each video (press q to quit)
	3.	Enter the number of people visible
	4.	Input a note (optional)
	5.	Annotate proximity zone for each person at each interval (i, p, s, or x)

 ### 💡 Zone Legend
i – intimate
p – personal
s – social
x – off-screen / left the area


Results are saved to analysis_results.xlsx in the selected folder.

### References 

[1] E. T. Hall, The Hidden Dimension. Doubleday, 1966.

# License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).
You are free to share and adapt the material for non-commercial purposes with appropriate attribution.

More info: https://creativecommons.org/licenses/by-nc/4.0/

# Acknowledgments

This code was developed as part of Ana Müllers PhD program at at the Cologne Cobots Lab, TH Köln – University of Applied Sciences, Germany within the project “Skilled” [https://www.th-koeln.de/anlagen-energie-und-maschinensysteme/skilled_87008.php]. This research was funded by the Federal Ministry of Education and Research of Germany in the framework FH-Kooperativ 2-2019 (project number 13FH504KX9). We thank our collaboration partners DB Systel GmbH.
