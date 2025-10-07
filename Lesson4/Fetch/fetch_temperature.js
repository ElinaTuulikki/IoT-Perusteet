const url = 'https://api.open-meteo.com/v1/forecast?latitude=60.17&longitude=24.94&current_weather=true';

fetch(url)
.then(response => response.json())
.then(data => {
    const feeds = data.feeds;

    const temperature = feeds.map(feed => ({
        time: feed.created_at,
        temp: parseFloat(feed.field1)
    }));
    document.getElementById('output').textContent = JSON.stringify(temperature);
})
.catch(error => {
    console.error('Error fetching data:', error);
    document.getElementById('output').textContent = 'Error fetching data';
});