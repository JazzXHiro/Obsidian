
```dataviewjs
const pages = dv.pages('"2 - Source Notes/Personal/Shows & Movies/Movies/Misc"')
  .where(p => p.rating)
  .sort(p => p.rating, 'desc');

dv.table(
  ["Rank", "Movie Title", "Rating", "Last Watched"],
  pages.map((p, i) => [
    i + 1,
    p.file.name,
    p.rating,
    p.watched ?? ""
  ])
);
```