document.getElementById("clearSearch").onclick = function(e) {
    e.preventDefault()
    const firstName = document.getElementById("firstName")
    const lastName = document.getElementById("lastName")
    const position = document.getElementById("position")
    const district = document.getElementById("district")
    const pageLimit = document.getElementById("pageLimit")
    firstName.value = ""
    lastName.value = ""
    position.value = ""
    district.value = "All"
    pageLimit.value = "10"
};

document.getElementById('searchForm').onsubmit = function(e) {
    e.preventDefault();
    
    const form = this;
    let query = [];
    
    // Check each field and add to the query string if not empty
    ['search_first_name', 'search_last_name', 'search_position'].forEach(function(name) {
        const value = form.elements[name].value;
        if (value) {
            query.push(encodeURIComponent(name) + '=' + encodeURIComponent(value));
        }
    });

    if (form.elements["search_district"].value != "All") {
        query.push(encodeURIComponent("search_district") + '=' + encodeURIComponent(form.elements["search_district"].value));
    };

    if (form.elements["page_limit"].value != "10") {
        query.push(encodeURIComponent("page_limit") + '=' + encodeURIComponent(form.elements["page_limit"].value));
    };
    
    // Redirect to the URL with the query string
    let action = form.getAttribute('action');
    if (query.length > 0) {
        action += '?' + query.join('&');
    };
    
    window.location = action;
};