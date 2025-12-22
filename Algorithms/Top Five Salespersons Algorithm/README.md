# Top Five Salespersons Algorithm

## 📌 Goal of this module
Implement an algorithm that identifies the **top five salespersons** from a larger list using a **fixed‑size array**.  
The array is continuously updated and kept sorted in **descending order** based on total sales.

This mirrors common data‑processing patterns:
- Maintaining a fixed-size leaderboard
- Efficiently updating rankings as new data arrives
- Using arrays as the underlying data structure for predictable indexing

---

## 🧩 How the algorithm works

### 1. Initialize the top‑five array
- Create an array of size **5**
- Each element stores:
  - `name`
  - `salesTotal`
- All entries start with:
  - `name = ""`
  - `salesTotal = -1`  
  (ensures any real salesperson will replace them)

### 2. Process each salesperson
For every salesperson in `allSalespersons`:

- Compare their `salesTotal` to the **lowest** entry in the top‑five array
- If they outperform the lowest:
  - Replace the lowest entry
  - Re-sort the array in **descending** order

This ensures the array always contains the current top five.

### 3. Display the results
After processing all salespersons:
- Output the five entries in order (highest → lowest)

---

## 🧠 Why this matters
This lab reinforces:
- How arrays can be used to maintain **ordered, fixed‑size datasets**
- How algorithms depend on the underlying data structure
- How sorting and comparison operations interact with array‑based storage
- Real‑world patterns like leaderboards, top‑N filtering, and ranking systems

---

## 📝 Pseudocode (for reference)
DisplayTopFiveSalespersons(allSalespersons) { topSales = array of size 5
for each index i: topSales[i].name = "" topSales[i].salesTotal = -1
for each salesPerson in allSalespersons: if salesPerson.salesTotal > topSales[last].salesTotal: topSales[last] = salesPerson SortDescending(topSales)
Display all entries in topSales }


---

## ✔️ Output expectations
- Always displays **exactly five** entries  
- If fewer than five salespersons exist, remaining entries show:
  - `name = ""`
  - `salesTotal = -1`

---

## 📂 Files in this module
- `top_five_salespersons_algorithm.txt` (or `.md`)  
- `README.md` (this file)

---

## 📣 Notes
This algorithm is intentionally array‑based to align with course learning objectives.  
Later labs may explore linked lists, heaps, or priority queues for similar tasks.