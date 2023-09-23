$(document).ready(main)

// main.
function main(){
	$("div#existing-company").children("select#company").attr("required", false)
	$("div#existing-company").hide();
	$("input[name='company_type']").change(function(e){
		toggleCompanyType(e.target.value);
	})
}

// toggle company type depending on the radio button selected.
function toggleCompanyType(type){
	if (type=="existing"){
		//$("div#new-company").addClass("d-none")
		//$("div#existing-company").removeClass("d-none");
		$("div#new-company").children("input#company").attr("required",false)
		$("div#new-company").hide()
		$("div#existing-company").show()
		$("div#existing-company").children("select#company").attr("required", true)
		return
}
		//$("div#new-company").removeClass("d-none")
		//$("div#existing-company").addClass("d-none");
		$("div#new-company").show();
		$("div#new-company").children("input#company").attr("required", true)
		$("div#existing-company").children("select#company").attr("required", false)
		$("div#existing-company").hide();
};
