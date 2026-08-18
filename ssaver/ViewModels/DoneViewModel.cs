using CommunityToolkit.Mvvm.Input;

namespace ssaver.ViewModels;
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Interactivity;
public partial  class DoneViewModel :  ViewModelBase
{
    [RelayCommand]
    private void OnExitClicked()
    {
        if (Avalonia.Application.Current?.ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            desktop.Shutdown();
        }
    }
}