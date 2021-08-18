let i = 100;
let dept = "";

function getLevel(self) {
  let choice = self;
  choice = choice.id;
  let ul = document.createElement("ul");
  ul.id = choice + "levelUl";
  let clickedDepartment = document.getElementById(choice + "d");
  clickedDepartment.append(ul);
  let levelUl = document.getElementById(choice + "levelUl");

  let twoYearCourse = false;
  let fourYearCourse = false;
  let fiveYearCourse = false;
  let sixYearCourse = false;
  if (
    choice == "aerd" ||
    choice == "aefm" ||
    choice == "agad" ||
    choice == "abg" ||
    choice == "ann" ||
    choice == "aph" ||
    choice == "prm" ||
    choice == "anp" ||
    choice == "aqfm" ||
    choice == "emt" ||
    choice == "fwm" ||
    choice == "wma" ||
    choice == "cve" ||
    choice == "abe" ||
    choice == "mce" ||
    choice == "mte" ||
    choice == "ele" ||
    choice == "cpt" ||
    choice == "hrt" ||
    choice == "pbst" ||
    choice == "ppcp" ||
    choice == "sslm" ||
    choice == "fst"
  ) {
    fiveYearCourse = true;
  } else if (
    choice == "bch" ||
    choice == "mcb" ||
    choice == "pab" ||
    choice == "paz" ||
    choice == "csc" ||
    choice == "chm" ||
    choice == "mts" ||
    choice == "phs" ||
    choice == "sts" ||
    choice == "hsm" ||
    choice == "nud" ||
    choice == "htm" ||
    choice == "bfn" ||
    choice == "bam" ||
    choice == "eco" ||
    choice == "ets"
  ) {
    fourYearCourse = true;
  } else if (
    choice == "vba" ||
    choice == "vch" ||
    choice == "vcm" ||
    choice == "vpm" ||
    choice == "vpt" ||
    choice == "vbb"
  ) {
    sixYearCourse = true;
  } else if (choice == "gns") {
    twoYearCourse = true;
  }

  if (fiveYearCourse) {
    if (i == 100 || dept !== choice) {
      i = 100;
      while (i < 600) {
        let li = document.createElement("li");
        li.innerHTML =
          '<a href="/resourcecenter/download/' +
          choice +
          "/" +
          i +
          '/">' +
          i +
          " level </a>";
        levelUl.append(li);
        i += 100;
      }
    }
  }
  if (fourYearCourse) {
    if (i == 100 || dept !== choice) {
      i = 100;
      while (i < 500) {
        let li = document.createElement("li");
        li.innerHTML =
          '<a href="/resourcecenter/download/' +
          choice +
          "/" +
          i +
          '/">' +
          i +
          " level </a>";
        levelUl.append(li);
        i += 100;
      }
    }
  }
  if (sixYearCourse) {
    if (i == 100 || dept !== choice) {
      i = 100;
      while (i < 700) {
        let li = document.createElement("li");
        li.innerHTML =
          '<a href="/resourcecenter/download/' +
          choice +
          "/" +
          i +
          '/">' +
          i +
          " level </a>";
        levelUl.append(li);
        i += 100;
      }
    }
  }
  if (twoYearCourse) {
    if (i == 100 || dept !== choice) {
      i = 100;
      while (i < 300) {
        let li = document.createElement("li");
        li.innerHTML =
          '<a href="/resourcecenter/download/' +
          choice +
          "/" +
          i +
          '/">' +
          i +
          " level </a>";
        levelUl.append(li);
        i += 100;
      }
    }
  }
  dept = choice;
  return i;
  return dept;
}
