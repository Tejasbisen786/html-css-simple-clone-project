const speedTest = require('speedtest-net');

async function runSpeedTest() {
    console.log('Running speed test...');
    const st = speedTest({ maxTime: 5000 });

    st.on('downloadspeed', (downloadSpeed) => {
      console.log(`Download Speed: ${(downloadSpeed / 1000000).toFixed(2)} Mbps`);
    });

    st.on('uploadspeed', (uploadSpeed) => {
      console.log(`Upload Speed: ${(uploadSpeed / 1000000).toFixed(2)} Mbps`);
    });

    await new Promise((resolve) => st.on('testdone', resolve));
    console.log('Speed test completed.');

}

runSpeedTest();
