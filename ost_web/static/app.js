
let oSkills = new Map([
    ["Blade", 0],
    ["Blunt", 0],
    ["Hand To Hand", 0],
    ["Armorer", 0],
    ["Block", 0],
    ["Heavy Armor", 0],
    ["Athletics", 0],
    ["Acrobatics", 0],
    ["Light Armor", 0],
    ["Security", 0],
    ["Sneak", 0],
    ["Marksman", 0],
    ["Mercantile", 0],
    ["Speechcraft", 0],
    ["Illusion", 0],
    ["Alchemy", 0],
    ["Conjuration", 0],
    ["Mysticism", 0],
    ["Alteration", 0],
    ["Destruction", 0],
    ["Restoration", 0]
]);

let oAttributes = new Map([
    ["STR", 1],
    ["END", 1],
    ["SPD", 1],
    ["AGI", 1],
    ["PER", 1],
    ["INT", 1],
    ["WIL", 1]
]);

function skillSub(id){ 
    let skillCounter = document.getElementById(`${id}Counter`);
    oSkills.set(id, oSkills.get(id) - 1);

    if(oSkills.get(id) <= 0){
        oSkills.set(id, 0);
    }

    skillCounter.textContent = oSkills.get(id);
    updateAttributes();
}

function skillAdd(id){
    let skillCounter = document.getElementById(`${id}Counter`);
    oSkills.set(id, oSkills.get(id) + 1);

    if(oSkills.get(id) >= 10){
        oSkills.set(id, 10);
    }

    skillCounter.textContent = oSkills.get(id);
    updateAttributes();
}

function levelup(){
    oSkills.forEach((value, key) => {
        oSkills.set(key, 0);
        let skillCounter = document.getElementById(`${key}Counter`);
        skillCounter.textContent = 0;
    });

    oAttributes.forEach((value, key) => {
        oAttributes.set(key, 1);
        attributeCounter = document.getElementById(`${key}Counter`);
        attributeCounter.textContent = "+1";
    })
}

function updateAttributes(){
    oAttributes.set("STR", (oSkills.get("Blade") + oSkills.get("Blunt") + oSkills.get("Hand To Hand")));
    oAttributes.set("END", (oSkills.get("Armorer") + oSkills.get("Block") + oSkills.get("Heavy Armor")));
    oAttributes.set("SPD", (oSkills.get("Athletics") + oSkills.get("Acrobatics") + oSkills.get("Light Armor")));
    oAttributes.set("AGI", (oSkills.get("Security") + oSkills.get("Sneak") + oSkills.get("Marksman")));
    oAttributes.set("PER", (oSkills.get("Mercantile") + oSkills.get("Speechcraft") + oSkills.get("Illusion")));
    oAttributes.set("INT", (oSkills.get("Alchemy") + oSkills.get("Conjuration") + oSkills.get("Mysticism")));
    oAttributes.set("WIL", (oSkills.get("Alteration") + oSkills.get("Destruction") + oSkills.get("Restoration")));

    oAttributes.forEach((value, key) => {
        let attributeCounter = document.getElementById(`${key}Counter`);
        if(value>=10){
            attributeCounter.textContent = "+5";
        } else if(value >=8){
            attributeCounter.textContent = "+4";
        } else if(value >=5){
            attributeCounter.textContent = "+3";
        } else if(value >= 1){
            attributeCounter.textContent = "+2";
        } else if(value <= 0){
            attributeCounter.textContent = "+1";
        }
    })
}