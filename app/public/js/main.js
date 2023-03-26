

$(document).ready(function () {
    let web_page = 'home'


    $('#loading-bar').hide();

    $('#projects').click(function () {
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


            },
            error: function () {
                // AJAX request failed
                alert("Failed to load data");
                $('#loading-bar').fadeOut();
            }
        });
    });

    $('.index')
        .click(function () {
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
                        }, 1000);






                    },
                    error: function () {
                        // AJAX request failed
                        alert("Failed to load data");
                        $('#loading-bar').fadeOut();
                    }
                });

            }
        })
});
