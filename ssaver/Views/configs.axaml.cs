using Avalonia.Controls;
using Avalonia.Interactivity;

namespace StreakSaver.Views
{
    public partial class SetupPage : UserControl
    {
        public SetupPage()
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
