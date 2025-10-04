const url="https://api.thingspeak.com/channels/3084769/feeds.json?api_key=M0D52XVVQ8AMR042&results"

fetch(url)
.then(response => response.json())
.then(data => {
    const feeds = data.feeds;

    const temperatures = feeds.map(feed => ({
        time: feed.created_at,
        temp: parseFloat(feed.field1),
        humidity: parseFloat(feed.field2)
    }));
    document.getElementById("output").textContent = JSON.stringify(temperatures);
})

.catch(error => {
    console.error("Error fetching data", error);
    document.getElementById("output").textContent = "Error loading data";
});