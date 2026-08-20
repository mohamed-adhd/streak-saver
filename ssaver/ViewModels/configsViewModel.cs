using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Controls;
using Avalonia.Interactivity;
using ssaver.Models;
namespace ssaver.ViewModels;


public partial class configsViewModel : ViewModelBase
{
    [ObservableProperty] private MainWindowViewModel _main;
    private Api s; 
    public configsViewModel(MainWindowViewModel main)
    {
        _main = main;
    }
    [RelayCommand]
    private void onVerifyClicked()
    {
        s.send("verify","s","s","s");
        _main.Current_page = new DoneViewModel();
    }
}
