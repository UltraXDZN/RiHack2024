from django.conf import settings


def vue_js_files(request):
    static_base_dir = settings.STATICFILES_BASE_DIR
    vue_name = "prod" if settings.VUE_PROD else "dev"
    vue_dir = static_base_dir / vue_name / "assets"
    js_files = [file.relative_to(static_base_dir) for file in vue_dir.glob("**/*.js")]
    css_files = [file.relative_to(static_base_dir) for file in vue_dir.glob("**/*.css")]
    return {
        "vue_js_files": js_files,
        "vue_css_files": css_files,
    }
