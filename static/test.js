async function get_row_data_from_db(user_id) {
    try {
        const res = await fetch(`/tables?user_id=${user_id}`)
        return await res.json()
    } catch (err) {
    }
}

class Table {
    constructor(json) {
        this.table_id = 0
        this.user_id = 0
        this.records = this.fromJson(json)
    }

    gen() {
        const table = document.createElement("div");
        table.className = "tb"
        const newContent = document.createElement("table");
        let header = new DayTableView(new DayTableDTO('title', 'what have done', 'time'))
        header.tag = "th"
        header.contentable = false
        newContent.appendChild(header.toHtmlView())

        for (let i = 0; i < this.records.length; i++) {
            // let record = new Record(this.records[i].title, this.records[i].done, this.records[i].time, i)
            let view = new DayTableView(this.records[i]).toHtmlView()
            newContent.appendChild(view)
        }
        table.appendChild(newContent);

        table.addEventListener("click", (event) => {
            this.sendData()
        });
        return table
    }

    fromJson(json) {
        let records = []
        // console.log(this.table_id)
        for (let i = 0; i < json["records"][0].length; i++) {
            let record = json["records"][0][i]
            // this.user_id = record["user_id"]
            // this.table_id = record["table_number"]
            let dto = new DayTableDTO(
                record["title"],
                record["done"],
                record["time"],
                record["user_id"],
                record["row"],
                record["table_number"]
            )
            records.push(dto)
        }
        console.log(records)
        return records
    }

    toJson() {
        let res = {"records": []}
        for (let record of this.records) {
            res["records"].push({
                row: record.row,
                table_number: record.table_number,
                user_id: record.user_id,
                title: record.title,
                done: record.done,
                time: record.time,
            })
        }
        return JSON.stringify(res)
    }

    sendData() {
        let XHR = new XMLHttpRequest();
        XHR.open('POST', 'process');
        XHR.setRequestHeader('content-type', 'application/json');
        XHR.send(this.toJson())
    }
}

class DayTableDTO {
    constructor(title, done, time, user_id, row, table_number) {
        this.title = title
        this.done = done
        this.time = time
        this.user_id = user_id
        this.row = row
        this.table_number = table_number
    }
}

class DayTableView {
    constructor(dto) {
        this.dto = dto
        this.tag = "td"
        this.contentable = true
    }

    addTitle() {
        let v = document.createElement(this.tag)
        v.textContent = this.dto.title
        v.contentEditable = this.contentable
        v.addEventListener("input", (event) => {
            this.dto.title = v.textContent
        });
        return v;
    }

    addDone() {
        let v = document.createElement(this.tag)
        v.textContent = this.dto.done
        v.contentEditable = this.contentable
        v.addEventListener("input", (event) => {
            this.dto.done = v.textContent
        });
        return v;
    }

    addTime() {
        let v = document.createElement(this.tag)
        v.textContent = this.dto.time
        v.contentEditable = this.contentable
        v.addEventListener("input", (event) => {
            this.dto.time = v.textContent
        });
        return v;
    }

    toHtmlView() {
        let record = document.createElement("tr")
        record.appendChild(this.addTitle())
        record.appendChild(this.addDone())
        record.appendChild(this.addTime())
        return record
    }
}


async function addElement(user_id) {
    let response_json = await get_row_data_from_db(user_id)
    let table = new Table(response_json)
    document.getElementById("tables").appendChild(table.gen())
    // setInterval(() => {
    //     table.sendData()
    // }, 2000)
}

// await get_row_data_from_db(1, 1)
// console.log(d)
//
addElement(1)
// addElement(1, 2)
// setInterval(() => {
//     sendData()
// }, 2000)


