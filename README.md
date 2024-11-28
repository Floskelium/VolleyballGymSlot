 
# 🏋️ Gym Scheduling Optimization for Teams

This Python script generates an optimal gym schedule for 3 teams, considering match dates balancing gym usage. The task involves assigning the teams to two gym slots in one gym and one additional gym slot in another gym, while adhering to the following conditions:

- **Home Games**: Always played in the **nicer gym**.
- **Balanced Gym Usage**: Teams should swap to the second gym as evenly as possible.
- **Monday Clash Handling**: The script focuses on **Monday** matchups, ensuring no scheduling conflicts in the nicer gym.

---

## 🛠️ Technologies Used

- **Python**: For the script logic and scheduling calculations.
- **Pandas**: For reading and processing the CSV file.

---

## 📥 Input Format

The script expects a CSV file with match dates in the following format:

| Date       | Time       | A         | B       |
|------------|------------|-----------|---------|
| 26.09.2024 | 20:00      | Team I    | Enemy   |
| 30.09.2024 | 20:15      | Enemy     | Team II |
| 01.12.2024 | 19:30      | Team III  | Enemy   |
| ...        | ...        | ...       | ...     |

**CSV Structure**:
- **Date**: The date of the match (in `DD.MM.YYYY` format).
- **Time**: Time of the game. Not really relevant for now but might be useful if considering time clashes in the future, which do not happen at the moment.
- **A/B**: Home / Away Team

