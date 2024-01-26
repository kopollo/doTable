let table = document.getElementById("table")
let rowLength = table.rows.length;

function getData() {
    let res = {"records": []}

    for (let i = 1; i < rowLength; i++) {
        let oCells = table.rows.item(i).cells;
        let cellLength = oCells.length;
        let record = {
            row: i,
            table_number: 1,
            user_id: 1,
            title: oCells.item(0).innerHTML,
            done: oCells.item(1).innerHTML,
            time: oCells.item(2).innerHTML,
        }
        res["records"].push(record)
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
setInterval(() => {
    sendData()
}, 2000)

