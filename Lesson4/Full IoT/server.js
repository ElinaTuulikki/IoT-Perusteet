import express from "express";
import { WebSocketServer } from "ws";
import cors from "cors";

const app = express();
const PORT = 3000;

app.use(cors());

// Mock data
let latestData = { temperature: 22.5, humidity: 55 };

// REST API endpoint
app.get("/api/sensor", (req, res) => {
    res.json(latestData);
});

// WebSocket server
const server = app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
const wss = new WebSocketServer({ server });

wss.on("connection", ws => {
    console.log("WebSocket client connected");
    ws.send(JSON.stringify(latestData));
});

// New mock data every minute
setInterval(() => {
    const temp = (20 + Math.random() * 5).toFixed(1);
    const hum = (40 + Math.random() * 20).toFixed(1);
    latestData = { temperature: parseFloat(temp), humidity: parseFloat(hum), time: new Date().toLocaleTimeString() };

    wss.clients.forEach(client => {
        if (client.readyState === 1) client.send(JSON.stringify(latestData));
    });

    console.log(`📡 Temp: ${temp} °C, Humidity: ${hum} %`);
}, 60000); // 60000 ms = 1 min
