# # import matplotlib.pyplot as plt
# # import matplotlib.dates as mdates
# # from datetime import datetime, timedelta

# # # Data for the tasks
# # tasks = [
# #     ("Gather stakeholder requirements", "2025-01-01", "2025-02-25"),
# #     ("System architecture design", "2025-02-26", "2025-04-21"),
# #     ("Prototype development", "2025-04-22", "2025-08-11"),
# #     ("Initial testing of prototype", "2025-08-12", "2025-09-08"),
# #     ("Full system development", "2025-09-09", "2026-02-23"),
# #     ("Internal testing of the integrated system", "2026-02-24", "2026-04-20"),
# #     ("Pilot deployment in selected labs", "2026-04-21", "2026-07-13"),
# #     ("Refinements based on pilot feedback", "2026-07-14", "2026-09-07"),
# #     ("Full-scale implementation and training", "2026-09-08", "2026-12-28"),
# #     ("Continuous monitoring and improvement", "2027-01-01", None),  # Ongoing task
# # ]

# # # Convert date strings to datetime objects and calculate durations
# # dates = [(task[0], datetime.strptime(task[1], "%Y-%m-%d"), 
# #           datetime.strptime(task[2], "%Y-%m-%d") if task[2] else None) for task in tasks]

# # # Create figure and axis
# # fig, ax = plt.subplots(figsize=(12, 6))

# # # Define Y positions and plot each task as a horizontal bar
# # y_pos = range(len(dates), 0, -1)  # Reverse order for better readability
# # for i, (task, start, end) in enumerate(dates):
# #     if end:  # For tasks with an end date
# #         ax.barh(y_pos[i], (end - start).days, left=start, color="skyblue", edgecolor="black")
# #     else:  # For ongoing tasks
# #         ax.barh(y_pos[i], 30, left=start, color="lightcoral", edgecolor="black", hatch="//")

# # # Configure axes
# # ax.set_yticks(y_pos)
# # ax.set_yticklabels([task[0] for task in dates], fontsize=10)
# # ax.set_xlabel("Timeline", fontsize=12)
# # ax.set_title("Project Timeline (PERT/Bar Chart)", fontsize=14)

# # # Set date formatting for x-axis
# # ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
# # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
# # plt.xticks(rotation=45, fontsize=10)

# # # Add grid
# # ax.grid(axis="x", linestyle="--", alpha=0.6)

# # # Show the plot
# # plt.tight_layout()
# # plt.show()


# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# # Create figure and axis
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.axis('off')  # Turn off the axis

# # Define block dimensions and positions
# blocks = [
#     ("Online Application\nSubmission", 0.05, 0.8),
#     ("Document Verification\n(ML Algorithms)", 0.35, 0.8),
#     ("Multi-Stage Evaluations:\n- Desktop Audits\n- On-Site Assessments\n- Final Reviews", 0.65, 0.8),
#     ("Cloud Computing\nScalable Storage", 0.05, 0.4),
#     ("Blockchain\nTamper-Proof Records", 0.35, 0.4),
#     ("User-Friendly Dashboard\n- Case Management Stats\n- Compliance Monitoring", 0.65, 0.4),
#     ("Outcomes:\n- Reduced Overhead\n- Improved Interactions\n- Precise Information", 0.35, 0.05),
# ]

# # Draw blocks
# for label, x, y in blocks:
#     ax.add_patch(patches.Rectangle((x, y), 0.25, 0.15, edgecolor='black', facecolor='lightblue'))
#     ax.text(x + 0.125, y + 0.075, label, ha='center', va='center', fontsize=9, wrap=True)

# # Draw arrows
# arrows = [
#     (0.175, 0.8, 0.35, 0.8),  # From Online Application to Document Verification
#     (0.525, 0.8, 0.65, 0.8),  # From Document Verification to Multi-Stage Evaluations
#     (0.175, 0.625, 0.175, 0.55),  # From Online Application to Cloud Computing
#     (0.425, 0.625, 0.425, 0.55),  # From Document Verification to Blockchain
#     (0.525, 0.625, 0.775, 0.55),  # From Multi-Stage Evaluations to Dashboard
#     (0.35, 0.475, 0.35, 0.2),  # From Cloud/Blockchain/Dashboard to Outcomes
# ]

# for x1, y1, x2, y2 in arrows:
#     ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(facecolor='black', arrowstyle='->'))

# # Show the block diagram
# plt.tight_layout()
# plt.show()

from graphviz import Digraph

# Creating a simple block diagram to explain the project using Graphviz
block_diagram = Digraph(name="Project_Block_Diagram", format="png")

# Define Blocks
block_diagram.node("A", "User Portal\n(Frontend Web App)", shape="box")
block_diagram.node("B", "Cloud Storage\n(Scalable + Secure)", shape="box")
block_diagram.node("C", "Machine Learning Engine\n(Document Validation)", shape="box")
block_diagram.node("D", "Multi-Stage Evaluation\n(Stage I, II, III)", shape="box")
block_diagram.node("E", "Blockchain Integration\n(Tamper-proof Records)", shape="box")
block_diagram.node("F", "Interactive Dashboard\n(Stats + Compliance)", shape="box")
block_diagram.node("G", "Automated Notifications\n(Alerts + Reminders)", shape="box")

# Define Flow
block_diagram.edge("A", "B", label="Uploads Documents")
block_diagram.edge("B", "C", label="Validates")
block_diagram.edge("C", "D", label="Processed for Evaluation")
block_diagram.edge("D", "E", label="Records on Blockchain")
block_diagram.edge("E", "F", label="Real-time Insights")
block_diagram.edge("F", "G", label="Triggers Alerts")
block_diagram.edge("G", "A", label="User Receives Updates")

# Save the Block Diagram
block_diagram_output_path = "Python/main"
block_diagram.render(filename=block_diagram_output_path.split(".png")[0], cleanup=True)

block_diagram_output_path
