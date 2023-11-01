$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		const code = $("#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${code}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	});
});
