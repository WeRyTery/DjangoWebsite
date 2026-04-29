// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    });

    var currentCategory = '*';
    var currentSearch = '';

    // Apply both category and text filters
    function applyFilters() {
        $grid.isotope({
            filter: function() {
                var $this = $(this);
                
                // Category check
                var categoryMatch = currentCategory === '*' ? true : $this.is(currentCategory);
                
                // Text check (searching inside h5)
                var title = $this.find('h5').text().toLowerCase();
                var searchMatch = currentSearch === '' ? true : title.indexOf(currentSearch) !== -1;
                
                return categoryMatch && searchMatch;
            }
        });
    }

    // Category click
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        currentCategory = $(this).attr('data-filter');
        applyFilters();
    });

    // Search input trigger ('input' catches typing, pasting, clearing)
    $('#searchInput').on('input', function() {
        currentSearch = $(this).val().toLowerCase().trim();
        applyFilters();
        
        // Show/hide clear button
        if (currentSearch.length > 0) {
            $('#clearSearchBlock').fadeIn(200);
        } else {
            $('#clearSearchBlock').fadeOut(200);
        }
    });

    // Prevent Enter key from refreshing the page
    $('#searchInput').keypress(function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
        }
    });

    // Clear search button
    $('#clearBtn').click(function() {
        $('#searchInput').val('');
        currentSearch = '';
        applyFilters();
        $('#clearSearchBlock').fadeOut(200);
    });
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});