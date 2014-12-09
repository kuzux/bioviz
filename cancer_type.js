$(function(){
    $("#karyotypes-tab").click(function(){
        $("#karyotypes-view").removeClass("hidden");
        $("#genes-view").addClass("hidden");
    });

    $("#genes-tab").click(function(){
        $("#genes-view").removeClass("hidden");
        $("#karyotypes-view").addClass("hidden");
    });

    $("#karyotypes-view .col-xs-2").each(function(){
        $(this).addClass("karyotype-link");
        var id   = $(this).html().match(/Chr (\d+)/)[1];
        var text = $(this).html();
        var link = "<a href=\"/chromosome.html?"+id+"\"><img src=\"/karyo1.png\" />"+text+"</a>";

        $(this).html(link);
    });

    $("#genes-filter").bind("change keyup", function(){
        // console.log($(this).val());
        var filter = $(this).val();
        var regex = new RegExp(filter, "gi");
        $("#genes-list").find("option").each(function(){
            if($(this).val().match(regex) !== null){
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});