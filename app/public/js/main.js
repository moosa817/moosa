

let web_page = 'home'

$('#loading-bar').hide();

function load_projects() {
    $('#loading-bar').show();

    $.ajax({
        url: "/projects",
        dataType: "json",
        success: function (data) {

            // AJAX request successful
            $('#loading-bar').fadeOut();
            $('#content').html(data.data);
            web_page = 'projects'


            const animatedElements = document.querySelectorAll("[data-aos]");

            const observer = new IntersectionObserver(entries => {
                entries.forEach(entry => {
                    if (entry.intersectionRatio > 0) {
                        entry.target.classList.add("aos-animate");
                    } else {
                        entry.target.classList.remove("aos-animate");
                    }
                });
            });

            animatedElements.forEach(element => {
                observer.observe(element);
            });
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;


        },
        error: function () {
            // AJAX request failed
            alert("Failed to load data");
            $('#loading-bar').fadeOut();
        }
    });
}


function load_index() {
    if (web_page === 'home') {
    }
    else {
        $('#loading-bar').show();


        $.ajax({
            url: "/index",
            dataType: "json",
            success: function (data) {

                // AJAX request successful
                $('#loading-bar').fadeOut();
                $('#content').html(data.data)

                const animatedElements = document.querySelectorAll("[data-aos]");

                const observer = new IntersectionObserver(entries => {
                    entries.forEach(entry => {
                        if (entry.intersectionRatio > 0) {
                            entry.target.classList.add("aos-animate");
                        } else {
                            entry.target.classList.remove("aos-animate");
                        }
                    });
                });

                animatedElements.forEach(element => {
                    observer.observe(element);
                });




                // $('[data-aos]').removeClass('animate-up animate-left anime-right')
                web_page = 'home'

                $("html, body").animate({
                    scrollTop: $(window.location.hash).offset().top
                }, 10);






            },
            error: function () {
                // AJAX request failed
                alert("Failed to load data");
                $('#loading-bar').fadeOut();
            }
        });

    }
}

// .index load home pages
const elements = document.querySelectorAll('.index');

elements.forEach(function (element) {
    element.addEventListener('click', function () {
        // Code to execute when element is clicked
        load_index()
    });
});

// load projects
const elements1 = document.querySelectorAll('.projects');

elements1.forEach(function (element) {
    element.addEventListener('click', function () {
        load_projects()
    });
});


$('#submit_main').click(function () {
    $('#loading-bar').show();

    var email = $('#email').val()
    var firstname = $('#name').val()
    var lastname = $('#lastname').val()

    var message = $('#message').val()

    document.getElementById("submit_main").innerHTML = "Submitting"

    $.ajax({
        data: {
            email: email,
            name: firstname,
            lastname: lastname,
            message: message
        },
        type: 'POST',
        url: '/contact'
    })
        .done(function (data) {
            $('#loading-bar').hide();

            if (data.error) {
                document.getElementById("submit_main").innerHTML = "Submit"
                document.getElementById('error-box').classList.toggle('hidden')
                document.getElementById('error-box').classList.toggle('flex')
                document.getElementById('success-box').classList.add("hidden")

                document.getElementById('error').innerHTML = data.error


                setTimeout(function () {
                    $("#error-box").addClass('hidden');
                }, 10000); // 10 seconds
            }
            else if (data.success) {
                document.getElementById('success-box').classList.remove('hidden')
                document.getElementById('success-box').classList.add('flex')
                document.getElementById('error-box').classList.add('hidden')

                document.getElementById('success').innerHTML = data.success


                $('#email').val('')
                $('#name').val('')
                $('#lastname').val('')
                $('#message').val('')

                document.getElementById("submit_main").innerHTML = "Submit"

                setTimeout(function () {
                    $("#success-box").addClass('hidden');
                }, 20000); // 10 seconds


            }
        })
})




