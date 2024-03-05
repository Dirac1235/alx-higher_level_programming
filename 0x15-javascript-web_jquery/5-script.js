const $listElem = $('ul.my_list');
const $addItemEl = $('div#add_item');

$addItemEl.on('click', () => {
  $listElem.append('<li>Item</li>');
});
