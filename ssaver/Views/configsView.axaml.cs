using Avalonia.Controls;
using Avalonia.Interactivity;

namespace ssaver.Views
{
    public partial class configsView : UserControl
    {
        public configsView()
        {
            InitializeComponent();
        }

        private void OnVerifyClicked(object? sender, RoutedEventArgs e)
        {
            var username = UsernameBox.Text;
            var repoName = RepoNameBox.Text;
            var filePath = FilePathBox.Text;
            var token = TokenBox.Text;

            // TODO: validate the token against the repo (e.g. GitHub API call)
            // and navigate onward on success.
        }
    }
}
