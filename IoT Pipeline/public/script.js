google.charts.load('current', { packages: ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

async function drawChart() {
    const url = "https://api.thingspeak.com/channels/3098285/feeds.json?api_key=PVVMEB2MK0GXQHXL&results";
    const response = await fetch(url);
    const json = await response.json();

    const data = new google.visualization.DataTable();
    data.addColumn('string', 'Time');
    data.addColumn('number', 'Temperature');
    data.addColumn('number', 'Humidity');

    document.getElementById('alert').innerHTML = "";
    let criticalFound = false;

    json.feeds.forEach(entry => {
        const timeFull = entry.created_at.split("T")[1].split("Z")[0];
        const time = timeFull.substring(0, 5);
        const temp = parseFloat(entry.field1);
        const hum = parseFloat(entry.field2);
        data.addRow([time, temp, hum]);
    });

const latest = json.feeds[json.feeds.length - 1];
    const latestTemp = parseFloat(latest.field1);

    if (latestTemp > 25) {
        document.getElementById('alert').innerHTML = `<p style="color:red;">Critical temperature!: ${latestTemp}°C</p>`;
    }

    const options = {
        title: 'Sensory data',
        curveType: 'function',
        legend: { position: 'bottom' }
    };

    const chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}

setInterval(drawChart, 15000);