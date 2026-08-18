using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Interactivity;

namespace StreakSaver.Views
{
    public partial class DonePage : UserControl
    {
        public DonePage()
        {
            InitializeComponent();
        }

        private void OnExitClicked(object? sender, RoutedEventArgs e)
        {
            if (Avalonia.Application.Current?.ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
            {
                desktop.Shutdown();
            }
        }
    }
}
