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
            time: oCells.item(2).innerHTML
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


async function get_data_from_db() {
    try {
        // GET
        const res = await fetch(`/tables/1`)

        // PARSE DATA
        let data = await res.json()
        // console.log(data["records"])
        return data
        // console.log(data)
    } catch (err) {
    }
}

async function addElement() {

    const newDiv = document.createElement("div",);
    newDiv.className = "tb"
    const newContent = document.createElement("table");
    let data = [
        ['title', 'what have done', 'time'],
    ]
    let response = await get_data_from_db()
    for (let i = 0; i < response["records"][0].length; i++) {
        let record = response["records"][0][i]
        data.push([record["title"], record["done"], record["time"]])
    }
    for (let i = 0; i < data.length; i++) {
        let record = document.createElement("tr")
        for (let j = 0; j < 3; j++) {
            let val = document.createElement("td")
            if (i === 0) {
                val = document.createElement("th")
            }
            val.innerHTML = data[i][j]
            record.appendChild(val)
        }
        newContent.appendChild(record)
    }
    newDiv.appendChild(newContent);
    document.getElementById("tables").appendChild(newDiv)
}

addElement()

// setInterval(() => {
//     sendData()
// }, 2000)


