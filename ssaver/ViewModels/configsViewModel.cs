using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Controls;
using Avalonia.Interactivity;

namespace ssaver.ViewModels;


public partial class configsViewModel : ViewModelBase
{
    [ObservableProperty] private MainWindowViewModel _main;
    public configsViewModel(MainWindowViewModel main)
    {
        _main = main;
        
    }
    [RelayCommand]
    private void onVerifyClicked()
    {
        _main.Current_page = new DoneViewModel();
    }
}
