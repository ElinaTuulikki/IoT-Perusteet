const express = require('express');
const SerialPort = require('serialport');
const axios = require('axios');

const app = express();
const port = 3000;

// ThingSpeak API
const THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_WRITE_API_KEY"; // change here your own key
const THINGSPEAK_URL = "https://api.thingspeak.com/update";

// Wokwi simulator port, COM4 as an example
const picoPort = new SerialPort({ path: "COM4", baudRate: 9600 });

let latestData = { temperature: null, humidity: null, status: "Waiting for data" };

// When Wokwi sends data to serial port
picoPort.on('data', async (data) => {
    const line = data.toString().trim();
    if (!line.includes(',')) return;

    const [temp, hum] = line.split(',');
    latestData = { temperature: parseFloat(temp), humidity: parseFloat(hum), status: "OK" };

    console.log(`📡 Temp: ${temp} °C, Hum: ${hum} %`);

    // Sends the data to Thingspeak
    try {
        const res = await axios.get(THINGSPEAK_URL, {
            params: { api_key: THINGSPEAK_API_KEY, field1: temp, field2: hum }
        });
        if (res.data > 0) console.log("✅ Sent to ThingSpeak");
        else console.log("⚠️ ThingSpeak rejected data");
    } catch (err) {
        console.error("❌ Error sending to ThingSpeak:", err.message);
    }
});

// Express endpoint to get the latest reading
app.get('/api/sensor', (req, res) => {
    res.json(latestData);
});

app.listen(port, () => {
    console.log(`🚀 Server running at http://localhost:${port}`);
});
