/*
Develop the app even further. Print the following information for all series from the search result on the web page. (7p)
    required information: Name, link to details (url), medium image and summary
    show the name in <h2> element
    show the url in <a> element. Also add target="_blank" to the link.
    show the medium image with <img src="" alt="">. Add medium image to src attribute and name property to alt attribute.
    some TV-shows don't have images. This will cause an error. You can fix this by adding ? operator to image property. Example: tvShow.show.image?.medium;. This is called optional chaining.
    show summary in <div> element (not <p>). This is because the summary is already in <p> element, and the result will not be valid if <p> is inside another <p>.
    collect the elements to <article> elements and append <article> elements to the HTML document.
    make <div id="results"> element to the HTML document where you append the <article> elements.
    clear the old results with innerHTML = '' before you append the new results.

*/ 