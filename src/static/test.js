let table = document.getElementById("table")
let rowLength = table.rows.length;

function getData() {
    let res = []

    for (let i = 1; i < rowLength; i++) {
        let oCells = table.rows.item(i).cells;
        let cellLength = oCells.length;
        let record = {
            name: oCells.item(0).innerHTML,
            deed: oCells.item(1).innerHTML,
            time: oCells.item(2).innerHTML,
        }
        res.push(record)
    }
    return res;
    // return JSON.stringify(res);
}

function sendData() {
    let XHR = new XMLHttpRequest();
    XHR.open('POST', 'process');
    XHR.setRequestHeader('content-type', 'application/json');
    XHR.send(JSON.stringify(getData()));
}
// setInterval(() => {
//     sendData()
// }, 2000)

