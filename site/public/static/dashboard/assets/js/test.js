var data = [{
  "id": "1",
  "name": "Jen",
  "city": "Melbourne",
  "age": "65"
}, {
  "id": "2",
  "name": "Roger",
  "city": "Melbourne",
  "age": "34"
}, {
  "id": "3",
  "name": "Rob",
  "city": "Sydney",
  "age": "23"
}, {
  "id": "4",
  "name": "George",
  "city": "Sydney",
  "age": "45"
}, {
  "id": "5",
  "name": "Fred",
  "city": "Perth",
  "age": "23"
}, {
  "id": "6",
  "name": "Kelly",
  "city": "Melbourne",
  "age": "23"
}, {
  "id": "7",
  "name": "Gina",
  "city": "Perth",
  "age": "25"
}];


 $('#table').bootstrapTable({
    data: data,
    showColumns: true,
 });


var sub_data = [{
  "street": "Gravy",
  "suburb": "Kew",
}, {
  "street": "Donald",
  "suburb": "Collingwood",
}, {
  "street": "Wells",
  "suburb": "St Kilda",
}];


function build_sub_table() {

  var data = JSON.parse(JSON.stringify(sub_data))

  $('#sub_table').bootstrapTable({
    columns: [{
      title: 'Street',
      field: 'street',
      sortable: true,
    },{
      title: 'Suburb',
      field: 'suburb',
      sortable: true,
    }],
    data: data
  })

};

function detailFormatter(index, row, element){
  return childDetail(index,row)
};


function childDetail(index,row){

  var row1 = document.createElement("div");
  row1.setAttribute('class','ui one column grid');

    var button = document.createElement("button");
    button.setAttribute('onclick','build_sub_table()')
  button.textContent="Get"

      row1.append(button);

  var row2 = document.createElement("div");
  row1.setAttribute('class','ui one column grid');

    var table = document.createElement('table');
    table.setAttribute('class','ui very compact table');
    table.setAttribute('id','sub_table');

      row2.append(table);

  row1.append(row2);

return row1;
};