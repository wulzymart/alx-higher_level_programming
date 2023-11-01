$('document').ready(function () {
  $('#btn_translate').click(translate);
  $('#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        getTranslation();
      }
    });
  });
});

function getTranslation () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`, function (data) {
    $('#hello').html(data.hello);
  });
}
