function get12HourFormat() {
    const now = new Date();
    let hour = now.getHours();

    if (hour > 12) {
        hour -= 12;
    } else if (hour === 0) {
        hour = 12;
    }

    return hour;
}

function validateFields() {
    var fields = ['param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7', 'param8', 'param9', 'param10', 'param11', 'param12', 'param13'];
    for (var i = 0; i < fields.length; i++) {
        var value = parseFloat(document.getElementById(fields[i]).value);
        if (isNaN(value)) {
            return false; // Trường này chưa được điền dữ liệu
        }
    }
    return true; // Tất cả các trường đều đã có dữ liệu
}

function sendParams() {
    var isValid = validateFields(); // Kiểm tra trước khi gửi dữ liệu

    if (!isValid) {
        // Hiển thị thông báo khi có trường chưa được điền dữ liệu
        alert('Vui lòng nhập đầy đủ dữ liệu!');
        return; // Ngăn không gửi dữ liệu nếu có trường chưa được nhập liệu
    }

    var currentTime = get12HourFormat();

    var param1Value = parseFloat(document.getElementById('param1').value);
    if (isNaN(param1Value) || param1Value < 0 || param1Value > 100) {
        alert('Vui lòng nhập đúng độ tuổi!');
        return; 
    }

    var param2Value = parseFloat(document.getElementById('param2').value);
    if (param2Value !== 0 && param2Value !== 1) {
        alert('Vui lòng nhập đúng giới tính (0 hoặc 1)!');
        return; 
    }

    var param3Value = parseFloat(document.getElementById('param3').value);
    if (![0, 1, 2, 3].includes(param3Value)) {
        alert('Vui lòng chỉ nhập giá trị 0, 1, 2 hoặc 3! (Loại đau thắt ngực)');
        return; 
    }

    var param4Value = parseFloat(document.getElementById('param4').value);
    var param5Value = parseFloat(document.getElementById('param5').value);
    
    var param6Value = parseFloat(document.getElementById('param6').value);
    if (param6Value !== 0 && param6Value !== 1) {
        alert('Vui lòng nhập đúng giá trị (0 hoặc 1)! (Mức đường huyết)');
        return;
    }

    var param7Value = parseFloat(document.getElementById('param7').value);
    if (![0, 1, 2].includes(param7Value)) {
        alert('Vui lòng chỉ nhập giá trị 0, 1, hoặc 2! (Điện tâm đồ)');
        return;
    }

    var param8Value = parseFloat(document.getElementById('param8').value);
    var param9Value = parseFloat(document.getElementById('param9').value);
    if (param9Value !== 0 && param9Value !== 1) {
        alert('Vui lòng nhập đúng giá trị (0 hoặc 1)! (Tập thể dục có gây đau thắt ngực không)');
        return;
    }

    var param10Value = parseFloat(document.getElementById('param10').value);
    var param11Value = parseFloat(document.getElementById('param11').value);
    if (![0, 1, 2].includes(param11Value)) {
        alert('Vui lòng chỉ nhập giá trị 0, 1, hoặc 2! (Độ dốc của đoạn ST)');
        return;
    }

    var param12Value = parseFloat(document.getElementById('param12').value);
    if (![0, 1, 2, 3].includes(param12Value)) {
        alert('Vui lòng chỉ nhập giá trị 0, 1, 2, hoặc 3! (Số lượng mạch chính)');
        return;
    }
    var param13Value = parseFloat(document.getElementById('param13').value);
    if (![1, 2, 3].includes(param13Value)) {
        alert('Vui lòng chỉ nhập giá trị 1, 2, hoặc 3! (Dữ liệu thalassemia)');
        return;
    }

    var formData = new FormData();
    formData.append('current_time', currentTime);
    formData.append('param1', param1Value);
    formData.append('param2', param2Value);
    formData.append('param3', param3Value);
    formData.append('param4', param4Value);
    formData.append('param5', param5Value);
    formData.append('param6', param6Value);
    formData.append('param7', param7Value);
    formData.append('param8', param8Value);
    formData.append('param9', param9Value);
    formData.append('param10', param10Value);
    formData.append('param11', param11Value);
    formData.append('param12', param12Value);
    formData.append('param13', param13Value);

    var xhr = new XMLHttpRequest();
    var url = '/write_params';

    xhr.open('POST', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alertWithOkButton('Dữ liệu đã được hệ thống ghi nhận. Vui lòng đợi 3 giây để nhận kết quả!', function() {
                    // Sau khi người dùng nhấn OK, thực hiện chuyển hướng sau 3 giây
                    setTimeout(function() {
                        window.location.href = '/show_result';
                    }, 3000); // 3 giây (3000 milliseconds)
                });
            } else {
                alert('Có lỗi xảy ra ghi nhận dữ liệu!');
            }
        }
    };
    xhr.send(formData);
}

function alertWithOkButton(message, callback) {
    var confirmation = confirm(message);
    if (confirmation && typeof callback === 'function') {
        callback();
    }
}

function sendParamsAndHideForm() {
    sendParams();
}

function showForm() {
    document.getElementById('paramForm').style.display = 'block';
}

function hideForm() {
    document.getElementById('paramForm').style.display = 'none';
}

window.onload = function() {
    showForm();
};


function hideWelcomeMessage() {
    var welcomeOverlay = document.getElementById('welcome-overlay');
    welcomeOverlay.style.display = 'none';
}
