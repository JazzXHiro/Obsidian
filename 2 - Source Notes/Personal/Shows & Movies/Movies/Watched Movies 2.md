

```dataview
TABLE
  rowIndex + 1 AS "Rank",
  file.name AS "Movie Title",
  rating AS "Rating",
  watched AS "Last Watched"
FROM "Shows & Movies/Movies"
WHERE type = "movie"
SORT rating DESC

```