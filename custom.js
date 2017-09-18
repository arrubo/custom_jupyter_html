
	$("span:contains('<!-- hide:all -->')").closest(".cell").remove();
	$("span:contains('<!-- hide:in -->')").closest(".cell").find(".prompt.output_prompt").html("");
	$("span:contains('<!-- hide:in -->')").closest(".input").remove();
	$(".js-link-to-tool").hide();
	$.each($("p"), function(index,item){
		if($(item).html() == '<!-- hide:all -->'){ 
			item.closest(".cell").remove(); 
		}
	});
	$("pre:has(span:empty)").closest(".cell").remove()

