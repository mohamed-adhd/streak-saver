namespace ssaver.ViewModels;
using CommunityToolkit.Mvvm.ComponentModel;

public partial class MainWindowViewModel  : ViewModelBase
{
    [ObservableProperty] private ViewModelBase current_page;
    [ObservableProperty] private MainWindowViewModel _main;

    public MainWindowViewModel(MainWindowViewModel main)
    {
        _main = main;
    }

    public MainWindowViewModel()
    {
        _main.Current_page = new welcomeViewModel(_main);
    }
}