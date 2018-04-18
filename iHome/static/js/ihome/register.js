function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function generateUUID() {
    var d = new Date().getTime();
    if (window.performance && typeof window.performance.now === "function") {
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
}
var imageCodeId = ""
var prevCodeId = ""
// 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
function generateImageCode() {
    imageCodeId = generateUUID();
    var Url = '/api/v1_0/image_code?cur=' + imageCodeId + '&pre=' + prevCodeId;
    $('.image-code>img').attr('src', Url);
    prevCodeId = imageCodeId
}

function sendSMSCode() {
    // 校验参数，保证输入框有数据填写
    $(".phonecode-a").removeAttr("onclick");
    var mobile = $("#mobile").val();
    if (!mobile) {
        $("#mobile-err span").html("请填写正确的手机号！");
        $("#mobile-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    }
    var imageCode = $("#imagecode").val();
    if (!imageCode) {
        $("#image-code-err span").html("请填写验证码！");
        $("#image-code-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    }
    // 组织响应数据
    var data = {
        'mobile': mobile,
        'imageCode': imageCode,
        'imageId': imageCodeId,
    }
    // TODO: 通过ajax方式向后端接口发送请求，让后端发送短信验证码
    $.ajax({
        'url': '/api/v1_0/sms_code', // 发送的地址
        'type': 'post', // 发送数据的方式
        'data': JSON.stringify(data), // 用json内置的模块将data(响应数据)转变为json格式的数据
        'contentType': 'applcation/json', // 发送数据的类型
        'headers': {
            'X-CSRFToken': getCookie('csrf_token')
        },
        'success': function (e) {
            // 回调函数
            if (e.errno == 0) {
                var num = 60
                a = setInterval(function () {
                    if (num >= 0) {
                        $('.phonecode-a').text(num)
                    }
                    else {
                        clearInterval(a)
                        $('.phonecode-a').html('获取验证码')
                        $('#phone-code-err').html('验证码已失效,请点击重新发送').siblings('#mobile-err').hide()
                        $(".phonecode-a").attr("onclick", "sendSMSCode();");
                    }
                    num--
                }, 1000)
                $('#phone-code-err').html(e.errmsg)
                $('#phone-code-err').show().siblings('#mobile-err').hide()
            }
            if (e.errno == 4103) {
                $('#mobile-err span').html(e.errmsg)
                $('#mobile-err').show().siblings('#mobile-err').hide()
                $(".phonecode-a").attr("onclick", "sendSMSCode();");
            }
            if (e.errno == 4001 || e.errno == 4004 || e.errno == 4002) {
                $('#image-code-err span').html(e.errmsg)
                $('#image-code-err').show().siblings('#mobile-err').hide()
                $(".phonecode-a").attr("onclick", "sendSMSCode();");
            }
        }
    })

}

$(document).ready(function () {
    generateImageCode(); // 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
    $("#mobile").focus(function () {
        $("#mobile-err").hide();
    });
    $("#imagecode").focus(function () {
        $("#image-code-err").hide();
    });
    $("#phonecode").focus(function () {
        $("#phone-code-err").hide();
    });
    $("#password").focus(function () {
        $("#password-err").hide();
        $("#password2-err").hide();
    });
    $("#password2").focus(function () {
        $("#password2-err").hide();
    });

    // TODO: 注册的提交(判断参数是否为空)
})
