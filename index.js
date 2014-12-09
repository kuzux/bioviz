$(function(){
    $("#go-btn").click(function(){
        location.href="/cancer_type.html?"+$("#cancer-type").val();
        return false;
    });

    $("#help-btn").click(function(){
        $("#help-content").removeClass("hidden");
        return false;
    });
});
