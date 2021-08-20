let selectDepartment = document.getElementById("department");
let selectLevel = document.getElementById("level");
let courseCode = document.getElementById("courseCode");
selectDepartment.addEventListener("change", updateForm);

function updateForm() {
    let choicedept = selectDepartment.value;

    let twoYearCourse = false;
    let fourYearCourse = false;
    let fiveYearCourse = false;
    let sixYearCourse = false;
    let nonAcademic = false;

    if (
        choicedept == "aerd" ||
        choicedept == "aefm" ||
        choicedept == "agad" ||
        choicedept == "abg" ||
        choicedept == "ann" ||
        choicedept == "aph" ||
        choicedept == "prm" ||
        choicedept == "anp" ||
        choicedept == "aqfm" ||
        choicedept == "emt" ||
        choicedept == "fwm" ||
        choicedept == "wma" ||
        choicedept == "cve" ||
        choicedept == "abe" ||
        choicedept == "mce" ||
        choicedept == "mte" ||
        choicedept == "ele" ||
        choicedept == "cpt" ||
        choicedept == "hrt" ||
        choicedept == "pbst" ||
        choicedept == "ppcp" ||
        choicedept == "sslm" ||
        choicedept == "fst"
    ) {
        fiveYearCourse = true;
    } else if (
        choicedept == "bch" ||
        choicedept == "mcb" ||
        choicedept == "pab" ||
        choicedept == "paz" ||
        choicedept == "csc" ||
        choicedept == "chm" ||
        choicedept == "mts" ||
        choicedept == "phs" ||
        choicedept == "sts" ||
        choicedept == "hsm" ||
        choicedept == "nud" ||
        choicedept == "htm" ||
        choicedept == "bfn" ||
        choicedept == "bam" ||
        choicedept == "eco" ||
        choicedept == "ets"
    ) {
        fourYearCourse = true;
    } else if (
        choicedept == "vab" ||
        choicedept == "vpr" ||
        choicedept == "vms" ||
        choicedept == "vmp" ||
        choicedept == "vpt" ||
        choicedept == "vpp"
    ) {
        sixYearCourse = true;
    } else if (choicedept == "gns") {
        twoYearCourse = true;
    } else if (
        choicedept == "nonAcademic"
    ) {
        nonAcademic = true;
    }

    if (twoYearCourse) {
        let options = selectLevel.getElementsByTagName("option");
        length = options.length;
        for (i = 0; i < length; i += 1) {
            options[0].remove();
        }
        for (i = 100; i < 300; i += 100) {
            let opt = document.createElement("option");
            opt.value = i;
            opt.textContent = i;
            selectLevel.appendChild(opt);
        }
    }
    if (fourYearCourse) {
        let options = selectLevel.getElementsByTagName("option");
        length = options.length;
        for (i = 0; i < length; i += 1) {
            options[0].remove();
        }
        for (i = 100; i < 500; i += 100) {
            let opt = document.createElement("option");
            opt.value = i;
            opt.textContent = i;
            selectLevel.appendChild(opt);
        }
    }
    if (fiveYearCourse) {
        let options = selectLevel.getElementsByTagName("option");
        length = options.length;
        for (i = 0; i < length; i += 1) {
            options[0].remove();
        }
        for (i = 100; i < 600; i += 100) {
            let opt = document.createElement("option");
            opt.value = i;
            opt.textContent = i;
            selectLevel.appendChild(opt);
        }
    }
    if (sixYearCourse) {
        let options = selectLevel.getElementsByTagName("option");
        length = options.length;
        for (i = 0; i < length; i += 1) {
            options[0].remove();
        }
        for (i = 100; i < 700; i += 100) {
            let opt = document.createElement("option");
            opt.value = i;
            opt.textContent = i;
            selectLevel.appendChild(opt);
        }
    }
    if (nonAcademic) {
        let options = selectLevel.getElementsByTagName("option");
        length = options.length;
        for (i = 0; i < length; i += 1) {
            options[0].remove();
        }
        nonAcademics = [
            "Spiritual",
            "Motivational",
            "Relationship",
            "Business",
            "Others",
        ];
        for (let i = 0; i < nonAcademics.length; i++) {
            let opt = document.createElement("option");
            opt.value = nonAcademics[i];
            opt.textContent = nonAcademics[i];
            selectLevel.appendChild(opt);
        }
    }
    if (nonAcademic) {
        courseCode.parentElement.style.display = "none"
        courseCode.value = ""
        document.getElementById("description").parentElement.style.display = "none"
        document.getElementById("description").value = ""
        document.getElementById("semester").parentElement.style.display = "none"
        document.getElementById("semester").value = ""

    } else {
        courseCode.style.display = "block"
    }
    
    if (selectDepartment.value != "---SELECT DEPARTMENT---"){
        courseCode.placeholder = "Course Code e.g " + selectDepartment.value + " " + (Number(selectLevel.value)+1)
    }
}

selectLevel.addEventListener("change", function(){
    if (selectDepartment.value != "---SELECT DEPARTMENT---"){
        courseCode.placeholder = "Course Code e.g " + selectDepartment.value + " " + (Number(selectLevel.value)+1)
    }
})

function validateform() {
    if (selectDepartment.value == "---SELECT DEPARTMENT---") {
        alert("Select Department")
        return false
    } else if (selectLevel.value == "---SELECT LEVEL---") {
        alert("Select Level")
        return false
    }
}


// if (document.location.search == "?fileSuccessfullyUploaded") {
//     let messageDiv = document.getElementById("message")
//     let message = document.createElement("p")
//     message.textContent = "File Successfully Uploaded"
//     message.style.color = "green"
//     messageDiv.appendChild(message)
// }
// if (document.location.search == "?message=error%20in%20uploading%20file") {
//     let messageDiv = document.getElementById("message")
//     let message = document.createElement("p")
//     message.textContent = "Error in uploading File"
//     message.style.color = "red"
//     messageDiv.appendChild(message)
// }