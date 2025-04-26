'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const query = document.getElementById('query').value;
  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
    .then(response => response.json())
    .then(data => {
      const resultsDiv = document.getElementById('results');
      resultsDiv.innerHTML = ''; // Clear old results

      data.forEach(tvShow => {
        const article = document.createElement('article');

        const name = document.createElement('h2');
        name.textContent = tvShow.show.name;

        const url = document.createElement('a');
        url.href = tvShow.show.url;
        url.target = "_blank";
        url.textContent = "Details";

        const image = document.createElement('img');
        image.src = tvShow.show.image?.medium || '';
        image.alt = tvShow.show.name;

        const summary = document.createElement('div');
        summary.innerHTML = tvShow.show.summary;

        article.appendChild(name);
        article.appendChild(url);
        article.appendChild(image);
        article.appendChild(summary);
        resultsDiv.appendChild(article);
      });
    })
    .catch(error => console.error('Error:', error));
});
