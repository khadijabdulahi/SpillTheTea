
const search_teas = ["Black Tea", "Green Tea", "Oolong Tea", "Pu-erh Tea", "White Tea", "Chamomile Tea", "Ginger Tea","Hibiscus Tea", "Mint Tea", "Rooibos Tea"]
const linkList = []
function giveTeaLinks(tea){
    return search_teas.indexOf(tea) + 1
}

 
function searchAutocomplete(input) {
    let formattedInput = input.toLowerCase()
    if (formattedInput == '') {
    return [];
    }
    let reg = new RegExp(formattedInput)
    return search_teas.filter(function(tea) {
        if (tea.toLowerCase().match(reg)) {
        return tea;
        }
    });
}
 
function showTeaResults(value) {
  result = document.getElementById("result");
  result.innerHTML = '';
  let list = '';
  let terms = searchAutocomplete(value);
  for (i=0; i<terms.length; i++) {
    list += '<li>' + `<a href="/teas/${giveTeaLinks(terms[i])}">` + terms[i] + '</a>' + '</li>';
  }
  result.innerHTML = '<ul>' + list + '</ul>';
}

