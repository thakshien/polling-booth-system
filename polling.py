import tkinter as tk

votes = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}

def vote(candidate):
    votes[candidate] += 1
    result.config(
        text=f"Vote recorded for {candidate}\n\n"
        + "\n".join(f"{x}: {y}" for x, y in votes.items())
    )

root = tk.Tk()
root.title("Polling Booth System")
root.geometry("400x400")

tk.Label(
    root,
    text="Electronic Voting System",
    font=("Arial", 20, "bold")
).pack(pady=20)

for candidate in votes:
    tk.Button(
        root,
        text=f"Vote for {candidate}",
        font=("Arial", 14),
        width=25,
        command=lambda c=candidate: vote(c)
    ).pack(pady=8)

result = tk.Label(
    root,
    text="Results will appear here",
    font=("Arial", 13)
)

result.pack(pady=20)

root.mainloop()