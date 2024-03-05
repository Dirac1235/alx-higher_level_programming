$(document).ready(function () {
  const salutUri = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $helloElmnt = $('div#hello');

  function getSalut () {
    return $.get({
      url: salutUri,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $helloElmnt.text(res.hello);
  });
});
