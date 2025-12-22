# Top Five Salespersons Algorithm

## Goal of this module

Implement an algorithm that identifies the **top five salespersons** from a larger list using a **fixed‑size array**.  
The array is continuously updated and kept sorted in **descending order** based on total sales.

This mirrors common data‑processing patterns such as:

- Maintaining a fixed‑size leaderboard  
- Efficiently updating rankings as new data arrives  
- Using arrays for predictable indexing and fast access  

## How the algorithm works

### 1. Initialize the top‑five array

- Create an array of size **5**  
- Each entry stores:
  - `name`
  - `salesTotal`
- All entries begin as:
  - `name = ""`
  - `salesTotal = -1`  
  This ensures any real salesperson will replace the placeholder.

### 2. Process each salesperson

For every salesperson in `allSalespersons`:

1. Compare their `salesTotal` to the **lowest** entry in the top‑five array  
2. If they outperform the lowest:
   - Replace the lowest entry  
   - Re-sort the array in **descending** order  

This guarantees the array always contains the **current** top five performers.

### 3. Display the results

After all salespersons have been processed:

- Output the five entries from highest to lowest  
- If fewer than five real salespersons exist, the remaining entries will still show:
  - `name = ""`
  - `salesTotal = -1`

## Why this matters

This lab reinforces several important concepts:

- How arrays can maintain **ordered, fixed‑size datasets**  
- How sorting and comparison operations interact with array‑based storage  
- How to update rankings efficiently as new data arrives  
- Real‑world applications such as:
  - Leaderboards  
  - Top‑N filtering  
  - Ranking systems  
  - Streaming data processing  

This algorithm is intentionally array‑based to align with course learning objectives.  
Later modules may explore more advanced structures such as **heaps**, **priority queues**, or **balanced trees**.

## Output expectations

- Always displays **exactly five** entries  
- If fewer than five salespersons exist, placeholders remain  
- Output is always sorted from **highest to lowest**  

