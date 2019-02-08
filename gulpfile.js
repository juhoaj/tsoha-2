var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();


// Update script / Copy the javascript files into our /static/js folder
gulp.task('update:js', function () {
    return gulp.src([
        'node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/popper.js/dist/popper.min.js'
    ])
        .pipe(gulp.dest("./application/static/js"));
});

// Update script / Copy font-awesome from node_modules into /static/fonts
gulp.task('update:fonts', function () {
    return gulp.src([
        './node_modules/font-awesome/**/*',
        '!./node_modules/font-awesome/{less,less/*}',
        '!./node_modules/font-awesome/{scss,scss/*}',
        '!./node_modules/font-awesome/.*',
        '!./node_modules/font-awesome/*.{txt,json,md}'
    ])
        .pipe(gulp.dest('./application/static/fonts/font-awesome'))
});

// Update script / Copy Bootstrap SCSS(SASS) from node_modules to /static/scss/bootstrap
gulp.task('update:scss', function () {
    return gulp.src(['./node_modules/bootstrap/scss/**/*'])
        .pipe(gulp.dest('./application/static/scss/bootstrap'));
});

// Update script
gulp.task('update', gulp.parallel('update:fonts', 'update:scss', 'update:js'));

// Build css files
gulp.task('build', function() {
    return gulp.src(['./application/static/scss/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest('./application/static/css'))
        .pipe(browserSync.stream());
});

// Configure the browserSync task and watch file path for change
gulp.task('watch', function() {
    browserSync.init({
        proxy:  "localhost:5000",
    });
    gulp.watch(['./application/static/scss/*.scss'], gulp.series('build'));
    gulp.watch("./application/templates/**/*").on('change', browserSync.reload);
});