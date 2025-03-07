document.getElementById("openSideBar").addEventListener("click", () =>{
    document.getElementById("sideBar").classList.add('opened-sidebar');
})
document.getElementById("closeSideBar").addEventListener("click", () =>{
    document.getElementById("sideBar").classList.remove('opened-sidebar')
})

//Add task toggler
document.getElementById("addTask").addEventListener("click", () => {
    document.getElementById("addTaskForm").classList.add('show-form');
})
document.getElementById("closeTaskForm").addEventListener("click", () => {
    document.getElementById("addTaskForm").classList.remove('show-form');
})