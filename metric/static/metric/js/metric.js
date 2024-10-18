function toggleSidebar() {
    document.body.classList.toggle('open-sidebar');
}

function CalcValue(){
    const start_value = document.getElementById('start_value').value || 0;
    const end_value = document.getElementById('end_value').value || 0;
    var result = end_value - start_value;
    document.getElementById('value').value = result;
}